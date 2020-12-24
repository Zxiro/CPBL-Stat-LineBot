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
        "url": "https://i.imgur.com/K7C7xCn.jpg", #CPBL logo
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
        "url": "https://i.imgur.com/awhdTdx.png", #fsm picture
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
        "url": "https://i.imgur.com/9UXqh3A.png", #player stat
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
        "url": "https://i.imgur.com/9QYcxOQ.jpg", #Team stat
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
        "url": "https://i.imgur.com/eUxT2OY.png",
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
              "label": "ˇ對戰數據",
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
    "size" : "giga",
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
          "layout": "horizontal",
          "margin": "md",
          "spacing": "sm",
          "contents": [

          ],
          "flex" : 1
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
            "label": "查看其他選手",
            "text": "player"
          }
        },
        {
          "type": "button",
          "style": "primary",
          "action": {
            "type": "message",
            "label": "查看其他年份",
            "text": "player_name"
          }
        },
        {
          "type": "button",
          "style": "primary",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "start"
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

def show_team():
  team = {
    "type": "bubble",
    "size" : "giga", 
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "數據表",
          "weight": "bold",
          "size": "md",
          "margin": "sm"
        },
        {
          "type": "separator",
          "margin": "sm"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "margin": "sm",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "Team",
                  "size": "md",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },
                {
                  "type": "text",
                  "text": "Game",
                  "size": "md",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },
                {
                  "type": "text",
                  "text": "W-T-L",
                  "size": "md",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },

                {
                  "type": "text",
                  "text": "富邦",
                  "size": "lg",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },
                {
                  "type": "text",
                  "text": "Lamigo",
                  "size": "md",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },
                {
                  "type": "text",
                  "text": "中信兄弟",
                  "size": "md",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },
                {
                  "type": "text",
                  "text": "統一獅",
                  "size": "md",
                  "color": "#555555",
                  "flex": 1,
                  "margin": "lg"
                },
              ]
            },
          ]
        },
        {
          "type": "separator",
          "margin": "sm"
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "sm",
          "spacing": "sm",
          "contents": [
          ]
        },
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
            "label": "查詢其他年份",
            "text": "team"
          }
        },
        {
          "type": "separator",
          "margin": "sm"
        },
        {
          "type": "button",
          "style": "primary",
          "action": {
            "type": "message",
            "label": "返回主選單",
            "text": "start"
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
  return team
