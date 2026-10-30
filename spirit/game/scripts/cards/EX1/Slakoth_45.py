from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import heal_all_and_cant_attack


card = PokemonCardDef(
    guid="0c0f6f38-0b44-5231-85be-e45069d34f11",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Slack Off",
            game_text="Remove all damage counters from Slakoth. Slakoth can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=heal_all_and_cant_attack(),
        ),
    ],
)
