from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import white_ray

card = PokemonCardDef(
    guid="9605190e-979a-5b01-80de-e85a8177faa3",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pheromosa.Name",
    display_name="Pheromosa",
    searchable_by=["Pheromosa", "Basic", "Ultra Beast", "Pheromosa"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=11,
    set_code="SM6",
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
