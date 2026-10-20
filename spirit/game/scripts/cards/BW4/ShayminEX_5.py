from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken


card = PokemonCardDef(
    guid="c2678552-4699-5ad4-8772-a6eb6b757f7b",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=5,
    set_code="BW4",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Attack(
            title="Synthesis",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_attach_energy(predicate=is_grass_energy_card, count=1,
                                        prompt='Choose a Grass Energy card to attach.'),
        ),
        Attack(
            title="Revenge Blast",
            game_text="Does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_prizes_taken('opponent'), 30, base=30),
        ),
    ],
)