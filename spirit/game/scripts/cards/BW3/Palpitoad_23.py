from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_per, count_in_play, has_attack_titled,
)

card = PokemonCardDef(
    guid="1e436948-b83f-580c-a784-935233fe9e19",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad", "Stage 1", "Palpitoad"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Round",
            game_text="Does 20 damage times the number of your Pok\u00e9mon that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(
                count_in_play("mine", has_attack_titled("Round")), 20,
            ),
        ),
    ],
)
