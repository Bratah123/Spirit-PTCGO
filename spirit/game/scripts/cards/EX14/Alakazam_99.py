from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import skill_copy_from_hand
from spirit.game.card_effects.support_common import recover_from_discard


card = PokemonCardDef(
    guid="f8f70d4f-dbaa-5776-8ddf-9780fc27ffb4",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam ★",
    searchable_by=["Alakazam \u2605", "Basic", "Star", "Alakazam"],
    subtypes=["Basic", "Star"],
    collector_number=99,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=65,
    abilities=[
        Attack(
            title="Psychic Select",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=recover_from_discard(count=1, minimum=1, reveal=False, to='hand', prompt='Choose a card from your discard pile.'),
        ),
        Attack(
            title="Skill Copy",
            game_text="Discard a Basic Pok\u00e9mon or Evolution card from your hand. Choose 1 of that card's attacks. Skill Copy copies this attack. This attack does nothing if Alakazam Star doesn't have the Energy necessary to use that attack. (You must still do anything else required for that attack.) Alakazam Star performs that attack.",
            cost={PokemonTypes.COLORLESS: 3},
                        effect=skill_copy_from_hand(),
        ),
    ],
)