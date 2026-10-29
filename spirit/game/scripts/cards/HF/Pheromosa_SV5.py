from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import white_ray

card = PokemonCardDef(
    guid="fba05b98-c61b-5a91-8ee5-bb7c531c69f5",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pheromosa.Name",
    display_name="Pheromosa",
    searchable_by=["Pheromosa", "Basic", "Ultra Beast", "Pheromosa"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=74,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=795,
    abilities=[
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="White Ray",
            game_text="If you have only 1 Prize card remaining, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=white_ray,
        ),
    ],
)
