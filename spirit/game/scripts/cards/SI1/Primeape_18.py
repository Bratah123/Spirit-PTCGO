from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import rampage


card = PokemonCardDef(
    guid="7fe7023b-bb68-5559-bda0-bd445674b519",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=57,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Rampage",
            game_text="Does 20 damage plus 10 more damage for each damage counter on Primeape. Flip a coin. If tails, Primeape is now Confused (after doing damage).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="+",
            effect=rampage,
        ),
    ],
)
