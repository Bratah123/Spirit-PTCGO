from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import power_cheer_passive
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="59419e29-dab9-5bf4-8b84-1659f928045d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Power Cheer",
            game_text="The attacks of your Pok\u00e9mon-GX in play that evolve from Eevee do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance). You can't apply more than 1 Power Cheer Ability at a time.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=power_cheer_passive,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)