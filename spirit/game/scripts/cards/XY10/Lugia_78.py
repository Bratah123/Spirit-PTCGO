from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


class _Pressure(Passive):
    """While this Pokemon is Active, damage from the opponent's Active Pokemon's attacks is reduced by 20 (before W/R)."""
    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        att = calc.attacker
        if (me is not None and att is not None and calc.is_attack and is_in_active_spot(me)
                and att.owning_player_id != me.owning_player_id and is_in_active_spot(att)):
            calc.amount -= 20


card = PokemonCardDef(
    guid="afd5b1be-e4db-5a50-bc6f-c70778a9503a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Ability(
            title="Pressure",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, any damage done by attacks from your opponent's Active Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            passive=_Pressure(),
        ),
        Attack(
            title="Intensifying Burn",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: _is_pokemon_ex(ctx.defender), 60),
        ),
    ],
)