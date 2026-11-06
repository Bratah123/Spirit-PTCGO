from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import effective_max_hp
from spirit.game.card_effects.attacks_common import flip_bonus


async def _eerie_cry(ctx):
    for pokemon in ctx.opponent_pokemon_in_play():
        if pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, pokemon):
            await ctx.deal_damage(30, target=pokemon, as_counters=True)


card = PokemonCardDef(
    guid="20684e47-f0d0-543a-b4ce-83a8465ee351",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Pain Amplifier",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_eerie_cry,
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)