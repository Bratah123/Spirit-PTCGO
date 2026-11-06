from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per


card = PokemonCardDef(
    guid="01bd71e6-d858-59b2-886f-e6dddb2f1b4b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Boyfriends",
            game_text="Does 20 damage plus 20 more damage for each Nidoking you have in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(
                count_in_play(
                    "mine",
                    lambda p: p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Nidoking",
                ),
                20, base=20,
            ),
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
