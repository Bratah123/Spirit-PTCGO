from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import snipe_attack


async def lunar_pain(ctx):
    """Double the number of damage counters on each of your opponent's Pokemon."""
    for pokemon in ctx.opponent_pokemon_in_play():
        current = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
        if current > 0:
            await ctx.deal_damage(current * 10, target=pokemon, as_counters=True)

card = PokemonCardDef(
    guid="4fd81eeb-9609-5689-b7c6-1c7892dd1f28",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala",
    searchable_by=["Lunala", "Stage 2", "Lunala"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="CEL25",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Lunar Pain",
            game_text="Double the number of damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=lunar_pain,
        ),
        Attack(
            title="Psychic Shot",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)