from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import smash_turn, rocket_tackle_recoil_protect


card = PokemonCardDef(
    guid="366d8a2b-f11b-5891-ac8a-064fd3dce806",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=9,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="After your attack, you may switch Blastoise with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=smash_turn(),
        ),
        Attack(
            title="Rocket Tackle",
            game_text="Blastoise does 10 damage to itself. Flip a coin. If heads, prevent all damage done to Blastoise by attacks during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=rocket_tackle_recoil_protect(10),
        ),
    ],
)
