from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import sleep_poison_flip

card = PokemonCardDef(
    guid="cac6f553-cb59-5d98-a7df-64747c06d3b2",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic", "Bulbasaur"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Sleep Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=sleep_poison_flip(),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)