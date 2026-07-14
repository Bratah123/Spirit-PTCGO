from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def witchs_domain(ctx):
    """Once during your turn, you may move up to 2 damage counters from your
    Pokemon to your opponent's Active Pokemon."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
        "Move up to 2 damage counters from your Pokémon to your "
        "opponent's Active Pokémon?"
    ):
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon to move damage counters from"
    )
    if source is None:
        return
    target = ctx.opponent_active()
    if target is None:
        return
    await ctx.move_damage_counters(source, target, max_count=2)


card = PokemonCardDef(
    guid="57f38c45-b660-582a-8e3e-318e595a8bea",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneVMAX.Name",
    display_name="Hatterene VMAX",
    searchable_by=["Hatterene VMAX", "VMAX", "HattereneVMAX"],
    subtypes=["VMAX"],
    collector_number=66,
    set_code="CZ",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneV.Name",
    family_id=858,
    abilities=[
        Ability(
            title="Witch's Domain",
            game_text="Once during your turn, you may move up to 2 damage counters from your Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_damaged_pokemon("mine"),
            effect=witchs_domain,
        ),
        Attack(
            title="G-Max Smite",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)