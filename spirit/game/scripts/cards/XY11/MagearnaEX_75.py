from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive, boost_own_next_turn
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.pokemon import energy_provides_type


def _metal_charged(target, carrier):
    me = carrier_pokemon(carrier)
    return me is not None and target.owning_player_id == me.owning_player_id and any(
        energy_provides_type(c, PokemonTypes.METAL.value) for c in target.children)


card = PokemonCardDef(
    guid="e1d9b45e-cd50-5126-abdb-0ac5d152b5f5",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagearnaEX.Name",
    display_name="Magearna-EX",
    searchable_by=["Magearna-EX", "Basic", "EX", "MagearnaEX"],
    subtypes=["Basic", "EX"],
    collector_number=75,
    set_code="XY11",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=801,
    abilities=[
        Ability(
            title="Mystic Heart",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to each of your Pok\u00e9mon that has any Metal Energy attached to it. (Existing effects are not removed.)",
            passive=attack_effect_shield_passive(protects=_metal_charged),
        ),
        Attack(
            title="Soul Blaster",
            game_text="During your next turn, this Pok\u00e9mon's Soul Blaster attack's base damage is 60.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=boost_own_next_turn(-60, 'Soul Blaster'),
        ),
    ],
)