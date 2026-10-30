from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import energy_protection_passive

card = PokemonCardDef(
    guid="bede803c-3b26-5eac-a27a-043b92a00c09",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1", "Metapod"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Ability(
            title="Energy Protection",
            game_text="Any damage done to Metapod by attacks is reduced by 10 for each Energy attached to Metapod. You can't reduce more than 30 damage in this way.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=energy_protection_passive(10),
        ),
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)