from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.models.board import BoardState


def _solar_revelation_protects(target, carrier):
    return (
        target.owning_player_id == carrier.owning_player_id
        and bool(BoardState.attached_energies(target))
    )


card = PokemonCardDef(
    guid="03d00288-c3f3-5434-84cb-c355f569a3c3",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonVMAX.Name",
    display_name="Espeon VMAX",
    searchable_by=["Espeon VMAX", "VMAX", "EspeonVMAX"],
    subtypes=["VMAX"],
    collector_number=270,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonV.Name",
    family_id=196,
    abilities=[
        Ability(
            title="Solar Revelation",
            game_text="Prevent all effects of attacks from your opponent's Pok\u00e9mon done to all of your Pok\u00e9mon that have Energy attached.(Existing effects are not removed. Damage is not an effect.)",
            passive=attack_effect_shield_passive(_solar_revelation_protects),
        ),
        Attack(
            title="Max Mindstorm",
            game_text="This attack does 60 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 60),
        ),
    ],
)