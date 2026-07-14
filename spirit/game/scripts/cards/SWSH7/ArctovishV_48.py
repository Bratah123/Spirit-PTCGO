from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.card_effects.pokemon import is_pokemon_gx


async def ancient_freeze(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and (
        is_pokemon_v(defender.archetype_id) or is_pokemon_gx(defender.archetype_id)
    ):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="5a4dc806-2af5-5293-9020-dde3b4e5201a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArctovishV.Name",
    display_name="Arctovish V",
    searchable_by=["Arctovish V", "Basic", "V", "ArctovishV"],
    subtypes=["Basic", "V"],
    collector_number=48,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=883,
    abilities=[
        Attack(
            title="Ancient Freeze",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon V or a Pok\u00e9mon-GX, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ancient_freeze,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            locks_next_turn=True,
        ),
    ],
)