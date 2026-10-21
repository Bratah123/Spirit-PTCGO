from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def _aura_break(ctx):
    """70; if the Defending Pokemon is Darkness or Fairy, it can't attack next turn."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    types = (d.get_attribute(AttrID.POKEMON_TYPES) or []) if d is not None else []
    if PokemonTypes.DARKNESS.value in types or PokemonTypes.FAIRY.value in types:
        lock_defender_attacks(ctx, d)


card = PokemonCardDef(
    guid="132e5e45-3d7b-585a-9194-7f467356a545",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Lookout",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Aura Break",
            game_text="If the Defending Pok\u00e9mon is a Darkness or Fairy Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_aura_break,
        ),
    ],
)