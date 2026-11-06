from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.ecard import devolution_beam


card = PokemonCardDef(
    guid="343cd1c5-b007-58de-9212-a67f5f087427",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BASEP",
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
            game_text="Does 10 damage times the number of Energy cards attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("defender", cards=True), 10),
        ),
        Attack(
            title="Devolution Beam",
            game_text="Choose an evolved Pok\u00e9mon (your own or your opponent's). Return the highest Stage Evolution card on that Pok\u00e9mon to its player's hand. That Pok\u00e9mon is no longer Asleep, Confused, Paralyzed, or Poisoned, or anything else that might be the result of an attack (just as if you had evolved it).",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=devolution_beam,
        ),
    ],
)
