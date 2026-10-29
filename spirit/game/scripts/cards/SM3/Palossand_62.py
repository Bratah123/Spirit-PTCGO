from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm3 import dust_storm


card = PokemonCardDef(
    guid="c5910b01-23f0-5b6b-bce6-689daac40dba",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name",
    display_name="Palossand",
    searchable_by=["Palossand", "Stage 1", "Palossand"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Dust Storm",
            game_text="Discard all cards from both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=dust_storm,
        ),
    ],
)
