from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.sm3 import knock_over


card = PokemonCardDef(
    guid="c1ddc55c-f9a6-525b-a50a-a808e9e0e1d6",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Bouffant Head",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=knock_over,
        ),
    ],
)
