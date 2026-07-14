from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.session.effects import is_special_energy


def _opponent_active_has_special_energy(ctx):
    active = ctx.opponent_active()
    if active is None:
        return False
    return any(is_special_energy(c) for c in ctx.attached_energies(active))


card = PokemonCardDef(
    guid="d2565f12-5cb7-5627-832f-8b4b49d4a757",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Ability(
            title="Insomnia",
            game_text="This Pokémon can't be Asleep.",
            passive=condition_immunity_passive(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Voltage Dive",
            game_text="If your opponent's Active Pokémon has any Special Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_opponent_active_has_special_energy, 80),
        ),
    ],
)
