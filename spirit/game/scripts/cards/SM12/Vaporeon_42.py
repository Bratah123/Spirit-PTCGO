from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import vitality_cheer_passive
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="adc73d63-bac9-5b07-bfc2-6421dbca95a1",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Vitality Cheer",
            game_text="Your Pok\u00e9mon-GX in play that evolve from Eevee get +60 HP. You can't apply more than 1 Vitality Cheer Ability at a time.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=vitality_cheer_passive,
        ),
        Attack(
            title="Refreshing Rain",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=heal_targets(30, 'each_own'),
        ),
    ],
)