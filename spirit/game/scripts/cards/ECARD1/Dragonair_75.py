from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="715bf0fd-4b92-5664-ab82-fda7bfd06a65",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Spiral Wave",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
    ],
)
