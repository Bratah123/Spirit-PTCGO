from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="de2073fc-ffb8-5684-8960-cfee55f0a328",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    display_name="Herdier",
    searchable_by=["Herdier", "Stage 1", "Herdier"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)