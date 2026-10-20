from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="01f0955b-0c86-56f3-b1fc-0d4b5579d443",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    display_name="Team Aqua's Poochyena",
    searchable_by=["Team Aqua's Poochyena", "Basic", "TeamAquasPoochyena"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=261,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)