from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, ability_id_for, ABILITIES_BY_ID,
)
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.passives import Passive

_GUID = "db5a6a5e-0350-58b3-955c-8dd6868d1ab3"


class _StarCipherPassive(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target.owning_player_id != carrier.owning_player_id:
            calc.weak_types = [PokemonTypes.PSYCHIC.value]


_STAR_CIPHER_GRANTED = Ability(
    title="Star Cipher",
    game_text="The Weakness of each of your opponent's Pokémon in play is now Psychic. (The amount of Weakness doesn't change.)",
    passive=_StarCipherPassive(),
)
_STAR_CIPHER_GRANTED.ability_id = ability_id_for(_GUID, 90)
ABILITIES_BY_ID[_STAR_CIPHER_GRANTED.ability_id] = _STAR_CIPHER_GRANTED


async def star_cipher(ctx):
    """VSTAR Power: gain an Ability making opponent's Pokemon Weak to Psychic."""
    entries = list(ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != _STAR_CIPHER_GRANTED.ability_id
           for e in entries if isinstance(e, dict)):
        entries.append(_STAR_CIPHER_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(
            ctx.attacker, AttrID.PIE_ABILITIES, entries
        )


card = PokemonCardDef(
    guid="db5a6a5e-0350-58b3-955c-8dd6868d1ab3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownVSTAR.Name",
    display_name="Unown VSTAR",
    searchable_by=["Unown VSTAR", "VSTAR", "UnownVSTAR"],
    subtypes=["VSTAR"],
    collector_number=66,
    set_code="SWSH12",
    rarity=Rarities.RareHoloVSTAR,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    family_id=201,
    abilities=[
        Attack(
            title="Tri Power",
            game_text="Flip 3 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=70,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=70),
        ),
        Attack(
            title="Star Cipher",
            game_text="Until this Pok\u00e9mon leaves play, it gains an Ability that has the effect \"The Weakness of each of your opponent's Pok\u00e9mon in play is now Psychic. (The amount of Weakness doesn't change.)\" (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            vstar=True,
            effect=star_cipher,
        ),
    ],
)