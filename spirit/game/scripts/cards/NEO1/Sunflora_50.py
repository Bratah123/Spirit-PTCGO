from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import petal_dance


card = PokemonCardDef(
    guid="abab4c3d-9a6a-5b30-bf48-70337d274fdc",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1", "Sunflora"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads. Sunflora is now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="x",
            effect=petal_dance,
        ),
    ],
)
