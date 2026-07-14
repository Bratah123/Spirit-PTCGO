from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken


def _star_bloom_condition(board, player_id, pokemon):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(
        PokemonTypes.GRASS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
        for p in bench.children
    )


async def star_bloom(ctx):
    targets = [p for p in ctx.my_bench()
               if PokemonTypes.GRASS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])]
    if not targets:
        return
    if not await ctx.ask_yes_no("Heal 120 damage from each of your Benched Grass Pokémon?"):
        return
    for pokemon in targets:
        await ctx.heal(120, pokemon)


card = PokemonCardDef(
    guid="373f2035-2e68-50fd-be12-085897056af2",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminVSTAR.Name",
    display_name="Shaymin VSTAR",
    searchable_by=["Shaymin VSTAR", "VSTAR", "ShayminVSTAR"],
    subtypes=["VSTAR"],
    collector_number=14,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVSTAR,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminV.Name",
    family_id=492,
    abilities=[
        Ability(
            title="Star Bloom",
            game_text="During your turn, you may heal 120 damage from each of your Benched Grass Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=star_bloom,
            condition=_star_bloom_condition,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 40 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), 40, base=120),
        ),
    ],
)