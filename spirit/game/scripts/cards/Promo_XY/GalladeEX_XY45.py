from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _bare_defender(ctx):
    target = ctx.opponent_active()
    return target is not None and not ctx.attached_energies(target)


card = PokemonCardDef(
    guid="98c2c863-0bd6-5297-82d4-ec1354a1a43f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name",
    display_name="Gallade-EX",
    searchable_by=["Gallade-EX", "Basic", "EX", "GalladeEX"],
    subtypes=["Basic", "EX"],
    collector_number=45,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Assault Sword",
            game_text="If your opponent's Active Pok\u00e9mon has no Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_bare_defender, 40),
        ),
        Attack(
            title="Cross Slash",
            game_text="This Pok\u00e9mon can't use Cross Slash during your next turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)