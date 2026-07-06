from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import regi_gate, heavy_slam

card = PokemonCardDef(
    guid="0985c9dd-ac02-542e-a9fb-801189732130",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel",
    searchable_by=["Registeel", "Basic", "Registeel"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=379,
    abilities=[
        Attack(
            title="Regi Gate",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=regi_gate,
        ),
        Attack(
            title="Heavy Slam",
            game_text="This attack does 50 less damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            damage_operator="-",
            effect=heavy_slam,
        ),
    ],
)
