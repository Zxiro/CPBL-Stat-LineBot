def show_pic():
  show = {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "size": "giga",
        "hero": {
          "type": "image",
          "url": "https://i.imgur.com/bVjkU07.png",
          "aspectMode": "fit",
          "size": "full",
          "aspectRatio": "2:1"
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Go for the full picture",
                "uri": "https://i.imgur.com/bVjkU07.png"
              },
              "height": "md",
              "color": "#5cd65c",
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "返回主選單",
                "text": "start"
              },
              "height": "md",
              "color": "#00cc66",
              "style": "primary"
            }
          ],
          "spacing": "lg"
        }
      }
    ]
  }

  return show

def main_menu():
  menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/bVjkU07.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "介紹與說明",
              "text": "功能介紹與說明"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/V2tkpQb.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "獲取有限狀態機圖",
              "text": "fsm"
            },
            "height": "md",
            "color": "#ff6666",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/nQaCDXh.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "球員數據",
              "text": "player"
            },
            "height": "md",
            "color": "#ff66b3",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/UrSkoW4.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "球隊數據",
              "text": "team"
            },
            "height": "md",
            "color": "#b366ff",
            "style": "primary"
          } ],
        "spacing": "lg"
      }
    },
      {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/UrSkoW4.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "聯盟數據",
              "text": "league"
            },
            "height": "md",
            "color": "#b366ff",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
  }
  return menu

def table():
  table = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "數據表",
        "weight": "bold",
        "size": "lg",
        "margin": "md"
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "年份",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$0.99",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "球隊",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$3.33",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "打席",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$0.69",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
           {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "打數",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
           {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "打點",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "得分",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "安打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "一壘安打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "二壘安打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "三壘安打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "全壘打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "壘打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "被三振",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "被安打",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "保送",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "OBP",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "SLG",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "AVG",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
  return table