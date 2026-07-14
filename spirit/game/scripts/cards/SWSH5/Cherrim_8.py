from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, has_rule_box
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_grass_energy_card


def _spring_bloom_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(is_grass_energy_card(c) for c in hand.children):
        return False
    return any(not has_rule_box(p.archetype_id) for p in board.pokemon_in_play(player_id))


async def spring_bloom(ctx):
    hand_energies = [c for c in ctx.hand() if is_grass_energy_card(c)]
    if not hand_energies:
        return
    targets = [p for p in ctx.my_pokemon_in_play() if not has_rule_box(p.archetype_id)]
    if not targets:
        return
    picked = await ctx.choose_cards(
        hand_energies, 1, prompt="Choose a Grass Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon without a Rule Box to attach the Energy to"
    )
    if target is not None:
        await ctx.attach_energy(picked[0], target)


card = PokemonCardDef(
    guid="48e717c5-8281-53aa-831e-ce4d059a83fd",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Spring Bloom",
            game_text="As often as you like during your turn, you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon that doesn't have a Rule Box (Pok\u00e9mon V, Pok\u00e9mon-GX, etc. have Rule Boxes).",
            activation=Activations.UNLIMITED,
            condition=_spring_bloom_condition,
            effect=spring_bloom,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)