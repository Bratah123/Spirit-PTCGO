from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_attach_energy


async def shadow_cyclone(ctx):
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench(), max_count=1)


card = PokemonCardDef(
    guid="704fd9d4-512f-5e0c-8837-c4095b3b3cab",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=780,
    abilities=[
        Attack(
            title="Amass",
            game_text="Search your deck for a basic Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_attach_energy(predicate=is_basic_energy_card, count=1, to_self=True),
        ),
        Attack(
            title="Power Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=shadow_cyclone,
        ),
    ],
)