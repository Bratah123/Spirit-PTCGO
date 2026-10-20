from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import place_counters


async def _spirit_scream(ctx):
    """Put damage counters on both Active Pokemon until each has 10 HP left."""
    for target in (ctx.defender, ctx.attacker):
        if target is None:
            continue
        hp = target.get_attribute(AttrID.HP, 0)
        if hp > 10:
            await ctx.deal_damage(hp - 10, target=target, apply_modifiers=False,
                                  as_counters=True)


card = PokemonCardDef(
    guid="8a9449fd-5c18-56c6-9b33-40ec24371d04",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name",
    display_name="Gourgeist",
    searchable_by=["Gourgeist", "Stage 1", "Gourgeist"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Attack(
            title="Eerie Voice",
            game_text="Put 2 damage counters each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(2, 'each_opponent'),
        ),
        Attack(
            title="Spirit Scream",
            game_text="Put damage counters on both Active Pok\u00e9mon until the remaining HP of each Pok\u00e9mon is 10.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=_spirit_scream,
        ),
    ],
)