from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.ex import magma_ring_no_retreat


card = PokemonCardDef(
    guid="ca1e5588-29ba-5bd9-8e26-8495cffdb8d3",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    display_name="Staravia",
    searchable_by=["Staravia", "Stage 1", "Staravia"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="POP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=magma_ring_no_retreat(),
        ),
    ],
)