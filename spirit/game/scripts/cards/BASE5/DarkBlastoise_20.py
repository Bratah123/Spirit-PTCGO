from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import rocket_tackle, unused_energy_bonus


card = PokemonCardDef(
    guid="afc1f328-1735-5182-97f1-a7ed0bc2e227",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkBlastoise.Name",
    display_name="Dark Blastoise",
    searchable_by=["Dark Blastoise", "Stage 2", "DarkBlastoise"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWartortle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Hydrocannon",
            game_text="Does 30 damage plus 20 more damage for each Water Energy attached to Dark Blastoise but not used to pay for this attack. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            damage_operator="+",
            effect=unused_energy_bonus(20, 40, energy_type=PokemonTypes.WATER),
        ),
        Attack(
            title="Rocket Tackle",
            game_text="Dark Blastoise does 10 damage to itself. Flip a coin. If heads, prevent all damage done to Dark Blastoise during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=rocket_tackle,
        ),
    ],
)
