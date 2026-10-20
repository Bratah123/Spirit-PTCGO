from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.card_effects.pokemon import is_energy_card


def _leaf_tailor_protects(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(is_energy_card(c) for c in target.children)


card = PokemonCardDef(
    guid="03377842-e098-5e17-afe3-f67cdee6496d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2", "Leavanny"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Ability(
            title="Leaf Tailor",
            game_text="Each of your Pok\u00e9mon that has any Energy attached to it has no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=no_weakness_passive(_leaf_tailor_protects),
        ),
        Attack(
            title="Cutting Arm",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)
