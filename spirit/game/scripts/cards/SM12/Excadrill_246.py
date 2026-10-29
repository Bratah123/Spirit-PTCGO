from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.sm12 import eleventh_hour_tackle


card = PokemonCardDef(
    guid="40f38cc0-958b-5e82-913b-0ed981e0c4d9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill", "Stage 1", "Excadrill"],
    subtypes=["Stage 1"],
    collector_number=246,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Eleventh Hour Tackle",
            game_text="If there are 3 or fewer cards in your deck, this attack does 150 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=eleventh_hour_tackle,
        ),
        Attack(
            title="Drill Bazooka",
            game_text="Discard the top 4 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=120,
            effect=mill_attack(4, opponent=False),
        ),
    ],
)