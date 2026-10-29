from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import hone_claws

card = PokemonCardDef(
    guid="068ffcd8-61c6-55b6-969a-ae22ed81ad5f",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    display_name="Skorupi",
    searchable_by=["Skorupi", "Basic", "Skorupi"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=451,
    abilities=[
        Attack(
            title="Hone Claws",
            game_text="During your next turn, this Pok\u00e9mon's Pierce attack's base damage is 90.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=hone_claws,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)