from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class AllJustADreamPassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier or not ctx.is_attack_effect():
            return count
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return count
        conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] not in conditions:
            return count
        return 0


card = PokemonCardDef(
    guid="aaac1bf0-77c7-5481-b9e9-356d2a7f0ea5",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name",
    display_name="Komala",
    searchable_by=["Komala", "Basic", "Komala"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="All Just a Dream",
            game_text="If this Pokémon is Asleep and is Knocked Out by damage from an attack from your opponent's Pokémon, your opponent can't take any Prize cards for it.",
            passive=AllJustADreamPassive(),
        ),
        Attack(
            title="Collapse",
            game_text="This Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)
