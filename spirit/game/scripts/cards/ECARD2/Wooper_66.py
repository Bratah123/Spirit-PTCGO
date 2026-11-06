from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import deep_dive


card = PokemonCardDef(
    guid="2a027aa4-5311-531d-8a5e-5b56adf33ce3",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic", "Wooper"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=194,
    abilities=[
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Deep Dive",
            game_text="Flip 3 coins. For each heads, remove 1 damage counter on Wooper.",
            cost={PokemonTypes.WATER: 1},
            effect=deep_dive,
        ),
    ],
)
