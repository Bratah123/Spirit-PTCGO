from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.sm3 import distort, sonic_volume

card = PokemonCardDef(
    guid="30f1445c-ea26-556d-8703-791b8eabfbd1",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoivernGX.Name",
    display_name="Noivern-GX",
    searchable_by=["Noivern-GX", "Stage 1", "GX", "NoivernGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=99,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Distort",
            game_text="Your opponent can't play any Item cards from their hand during their next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=distort,
        ),
        Attack(
            title="Sonic Volume",
            game_text="Your opponent can't play any Special Energy cards from their hand during their next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=sonic_volume,
        ),
        Attack(
            title="Boomburst-GX",
            game_text="This attack does 50 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=spread_damage(50, include_active=True),
        ),
    ],
)
