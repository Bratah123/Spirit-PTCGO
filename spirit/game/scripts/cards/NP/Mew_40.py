from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.ex import devolution_beam


card = PokemonCardDef(
    guid="a9f56ea5-9718-5dc3-99c9-2c97a104a3ba",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Psywave",
            game_text="Does 10 damage times the amount of Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("defender"), per=10),
        ),
        Attack(
            title="Devolution Beam",
            game_text="Flip a coin. If heads, choose 1 of either player's Evolved Pok\u00e9mon, remove the highest stage Evolution card from that Pok\u00e9mon, and put it into that player's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=devolution_beam,
        ),
    ],
)
