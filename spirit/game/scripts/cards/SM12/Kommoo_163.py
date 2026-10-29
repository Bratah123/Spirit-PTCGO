from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import scaly_uppercut
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot


card = PokemonCardDef(
    guid="a69e8a63-0267-5e30-bac2-c3566fcb2d2f",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o", "Stage 2", "Kommoo"],
    subtypes=["Stage 2"],
    collector_number=163,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Shout of Power",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target=lambda p: not is_in_active_spot(p), prompt='Choose a basic Energy card to attach to a Benched Pokémon'),
        ),
        Attack(
            title="Scaly Uppercut",
            game_text="You may discard a Pok\u00e9mon Tool card from this Pok\u00e9mon. If you do, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=90,
            damage_operator="+",
            effect=scaly_uppercut,
        ),
    ],
)