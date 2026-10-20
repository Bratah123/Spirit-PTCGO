from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if


def _has(pokemon, condition):
    return CLIENT_SPECIAL_CONDITION_NAMES[condition] in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def _self_asleep(ctx):
    return _has(ctx.attacker, SpecialConditions.ASLEEP)


def _not_paralyzed(board, player_id, pokemon):
    """Dream Waltz ignores Asleep only, not Paralysis."""
    return pokemon is None or not _has(pokemon, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="22334d1c-3802-58c1-905e-9ac81dbb1183",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1", "Musharna"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Attack(
            title="Telekinesis",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=snipe_attack(30, pool='any', apply_modifiers=False),
        ),
        Attack(
            title="Dream Waltz",
            game_text="This attack can be used even if this Pok\u00e9mon is Asleep. If this Pok\u00e9mon is Asleep, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_self_asleep, 30),
            usable_despite_conditions=True,
            condition=_not_paralyzed,
        ),
    ],
)