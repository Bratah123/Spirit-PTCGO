from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


from spirit.game.data_utils import Attack, def_for


async def copycat(ctx):
    """Copy the opponent's last non-GX attack."""
    last = None
    for _eid, archetype, title in ctx.session.turn_state.attacks_used_last_turn:
        last = (archetype, title)
    if last is None:
        return
    archetype, title = last
    definition = def_for(archetype)
    chosen = None
    for ability in getattr(definition, "abilities", []) or []:
        if isinstance(ability, Attack) and ability.title == title:
            chosen = ability
            break
    if chosen is None or getattr(chosen, "gx", False):
        return
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="ec2d047e-e087-51d4-8a04-fba619411fa8",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Copycat",
            game_text="If your opponent's Pok\u00e9mon used an attack that isn't a GX attack during their last turn, use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=copycat,
        ),
    ],
)