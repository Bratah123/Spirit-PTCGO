from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import naptime


card = PokemonCardDef(
    guid="76576e32-656d-500c-b0cb-d4f6ab355c4c",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasSlowbro.Name",
    display_name="Sabrina's Slowbro",
    searchable_by=["Sabrina's Slowbro", "Stage 1", "SabrinasSlowbro"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasSlowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Naptime",
            game_text="Flip a coin. If heads, remove 3 damage counters from Sabrina's Slowbro and Sabrina's Slowbro is now Asleep. If Sabrina's Slowbro has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=naptime,
        ),
        Attack(
            title="Screaming Headbutt",
            game_text="You can't use this attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            locks_next_turn=True,
        ),
    ],
)
