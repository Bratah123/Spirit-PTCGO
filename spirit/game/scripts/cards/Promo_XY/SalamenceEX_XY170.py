from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_in_play
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


card = PokemonCardDef(
    guid="835dbd0a-fe86-5cbe-beab-976a8e690a53",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceEX.Name",
    display_name="Salamence-EX",
    searchable_by=["Salamence-EX", "Basic", "EX", "SalamenceEX"],
    subtypes=["Basic", "EX"],
    collector_number=170,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=373,
    abilities=[
        Attack(
            title="Beastly Fang",
            game_text="This attack does 50 more damage for each of your opponent's Pok\u00e9mon-EX.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_in_play('opponent', pred=_is_ex), 50, base=10),
        ),
        Attack(
            title="Dragon Strike",
            game_text="This Pok\u00e9mon can't use Dragon Strike during your next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)