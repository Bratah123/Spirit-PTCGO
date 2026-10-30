from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import even_game_search_basics, stadium_play_heal_or_damage

card = PokemonCardDef(
    guid="3a7d4b54-3b31-5ff6-9d86-674241e28974",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Even Game",
            game_text="Count the number of your opponent's Pok\u00e9mon. Search your deck for up to that number of Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
                        effect=even_game_search_basics(),
        ),
        Attack(
            title="Stadium Play",
            game_text="If you have a Stadium card in play, remove 1 damage counter from each of your Pok\u00e9mon. If your opponent has a Stadium card in play, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
                        effect=stadium_play_heal_or_damage(1, 1),
        ),
    ],
)