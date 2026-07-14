from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def ear_moves(ctx):
    """Once during your turn, you may move 1 damage counter from 1 of your
    Pokemon to 1 of your opponent's Pokemon."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
        "Move 1 damage counter from 1 of your Pokemon to 1 of your "
        "opponent's Pokemon?"
    ):
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokemon to move a damage counter from"
    )
    if source is None:
        return
    opponents = ctx.opponent_pokemon_in_play()
    if not opponents:
        return
    dest = await ctx.choose_pokemon(
        opponents, "Choose 1 of your opponent's Pokemon"
    )
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)

card = PokemonCardDef(
    guid="35126f48-89cc-58e8-ade6-f48d5410a311",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1", "Meowstic"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Ability(
            title="Ear Moves",
            game_text="Once during your turn, you may move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_damaged_pokemon("mine"),
            effect=ear_moves,
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)